var AWS = require('aws-sdk');
require('dotenv').config();

AWS.config.update({
    accessKeyId: process.env.AWS_ACCESS_KEY_ID,
    secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
    region: process.env.AWS_REGION
});

var params = {
    Image: {
        S3Object: {
            Bucket : "class-iot-bucket",
            Name : "dogandcat.jpg"
        }
    },
    MaxLabels: 5,
    MinConfidence : 80
};

const rekognition = new AWS.Rekognition();
rekognition.detectLabels(params, function(err, data) {
    if (err) console.log(err, err.stack);
    else console.log(data);
});
