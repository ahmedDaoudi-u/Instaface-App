// jhint esversion:6
const {
  exec
} = require('child_process');
const express = require("express");
const bodyparser = require("body-parser");
const path = require('path');
const ejs = require("ejs");
const fs = require('fs');
const multer = require('multer'); // For handling file uploads
const {
  spawn
} = require('child_process');



const app = express();

app.set('view engine', 'ejs');

app.use(express.static("public"));
app.use(bodyparser.urlencoded({
  extended: true
}));

const storage = multer.diskStorage({
  destination: function(req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function(req, file, cb) {
    cb(null, file.originalname);
  }
});

const upload = multer({
  storage
});
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));
app.set("view cache", false);

app.get("/", function(req, res) {

  res.render("home");

});
app.post("/", function(req, res) {
  const token = req.body.token;
  const id = req.body.appid;
  const apps = req.body.apps;

  exec(`python Python/longtoken.py "${token}" "${id}"  "${apps}"`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Python script: ${error.message}`);
      // Handle the error
    } else {
      const output = stdout ? stdout.toString() : '';
      res.render("home", {
        ha: output
      });
      // Redirect or send a response back
      // Assuming you have the variables extracted from the output
    };

  });

});




const runPythonScript = (id, token) => {
  return new Promise((resolve, reject) => {
    exec(`python Python/generatecsv.py "${id}" "${token}"`, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error: ${error.message}`);
        reject(error);
        return;
      }

      // The Python script has completed successfully
      resolve();
    });
  });
};


app.get("/Facebook", function(req, res) {

  res.render("facebook");

});


app.get('/engagement', function(req, res) {
  // Get the engagement rate from the query parameter
  const engagementRate = parseFloat(req.query.engagement);

  // Render the "engagement" template and pass the "engagement" variable
  res.render('engagement', {
    engagement: engagementRate.toFixed(2)
  });
});



// app.js
app.get("/analysis", function(req, res) {
  // Get the query parameter "analysis" from the URL
  const analysisResultsJson = req.query.analysis;

  // Parse the JSON string back into a JavaScript object
  const analysisResults = JSON.parse(analysisResultsJson);

  // Render the analysisResults page and pass the analysisResults as a variable
  res.render("analysis", { analysisResults });
});

app.get("/ads",function(req,res){
  const plotFilePathsJSON = req.query.plotFilePaths;

  try {
    // Parse the plotFilePaths JSON string back to an array
    const plotFilePaths = JSON.parse(decodeURIComponent(plotFilePathsJSON));

    // Now you have the array of plot file paths, and you can use it to render your EJS template
    res.render('ads', { plotFilePaths });
  } catch (error) {
    console.error('Error parsing plot file paths:', error);
    res.status(500).send('Internal Server Error');
  }
})




// Endpoint to run the Facebook Python script and serve the generated CSV file
app.post("/Facebook", upload.single('csvFile'), async (req, res) => {
  const token = req.body.longtoken;
  const id = req.body.appID;
  const submitButton = req.body.submit;




  if (submitButton === 'script1') {
    try {
      // Run the Python script and wait for it to complete
      await runPythonScript(id, token);

      // Wait for 20 seconds before sending the CSV file
      setTimeout(() => {
        const csvFilePath = path.join(__dirname, 'data.csv');

        res.setHeader('Content-Disposition', 'attachment; filename="data.csv"');
        res.setHeader('Content-Type', 'text/csv');

        res.sendFile(csvFilePath, (err) => {
          if (err) {
            console.error(`Error sending CSV file: ${err}`);
            res.status(500).send('Error sending CSV file');
          }
        });
      }, 20000);
      // Adjust the delay as needed
    } catch (error) {
      console.error(`Error running Python script: ${error.message}`);
      res.status(500).send('An error occurred during script execution.');
    }


}
  else if (submitButton === 'script2') {
    const filePath = req.file.path;
    const pythonProcess = spawn('python', ['Python/engagement.py', filePath]);

    let resultData = '';

    pythonProcess.stdout.on('data', (data) => {
      resultData += data.toString();
    });

    pythonProcess.stderr.on('data', (data) => {
      console.error(`Python Error: ${data}`);
      res.status(500).send('Internal Server Error');
    });

    pythonProcess.on('close', (code) => {
      if (code === 0) {
        const engagementRate = parseFloat(resultData);
        const engagement = engagementRate.toFixed(2);
        res.redirect(`/engagement?engagement=${engagement}`);}

      });



}


  else if (submitButton === 'script') {
        const csvFilePath = req.file.path;

  // Execute the Python script
  const pythonProcess = spawn('python', ['Python/firstAnalysis.py', csvFilePath]);

  let analysisResults = '';

  pythonProcess.stdout.on('data', (data) => {
    analysisResults += data.toString();
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python Error: ${data}`);
    res.status(500).send('Internal Server Error');
  });

  pythonProcess.on('close', (code) => {
    if (code === 0) {
      // Parse the analysis results from the Python script output (if needed)
      // For example, if the Python script outputs JSON data, you can parse it here
      try {
        analysisResults = JSON.parse(analysisResults);
        const queryParams = encodeURIComponent(JSON.stringify(analysisResults));
          res.redirect(`/analysis?analysis=${queryParams}`);

      } catch (error) {
        console.error('Error parsing analysis results:', error);
        res.status(500).send('Internal Server Error');
        return;
      }


      // Render the analysisResults page and pass the analysisResults as a variable


    } else {
      console.error(`Python process exited with code ${code}`);
      res.status(500).send('Internal Server Error');
    }
  });






}
  else if (submitButton=== 'script4') {
    const csvFilePath = req.file.path;

  // Execute the Python script
  const pythonProcess = spawn('python', ['Python/adsAnalysis.py', csvFilePath]);

  let plotFilePaths = [];
  let responseSent = false; // Flag to track if the response has been sent

  pythonProcess.stdout.on('data', (data) => {
    plotFilePaths.push(data.toString());
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python Error: ${data}`);
    if (!responseSent) {
      responseSent = true;
      res.status(500).send('Internal Server Error');
    }
  });

  pythonProcess.on('close', (code) => {
    if (code === 0 && !responseSent) {
      try {
        // Convert the array of plot file paths to a JSON string
        const analysisResults = JSON.stringify(plotFilePaths);

        const queryParams = encodeURIComponent(analysisResults);
        // Redirect to the ads route and pass the plotFilePaths as a query parameter
        res.redirect(`/ads?plotFilePaths=${queryParams}`);
      } catch (error) {
        console.error('Error parsing analysis results:', error);
        res.status(500).send('Internal Server Error');
      }
    } else if (!responseSent) {
      console.error(`Python process exited with code ${code}`);
      responseSent = true;
      res.status(500).send('Internal Server Error');
    }
  });






  }
  else {
    res.status(400).send('Invalid form submission.');
  }




});









app.get("/contact", function(req, res) {

  res.render("contact");

});





app.listen(3000, () => {
  console.log(`Server is running on port 3000`);
});
