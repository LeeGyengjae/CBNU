var AWS = require('aws-sdk');
const { LexRuntimeV2 } = require("@aws-sdk/client-lex-runtime-v2");
require('dotenv').config();

const lexruntime = new LexRuntimeV2({ 
    region: process.env.AWS_REGION,
    credentials: new AWS.Credentials({
        accessKeyId: process.env.AWS_ACCESS_KEY_ID,
        secretAccessKey: process.env.AWS_SECRET_ACCESS_KEY,
    })     
});

const lexparams = {
    "botAliasId": process.env.LEX_BOT_ALIAS_ID,
    "botId": process.env.LEX_BOT_ID,
    "localeId": process.env.LEX_LOCALE_ID,
    "text": "호텔을 예약해줘",
    "sessionId": "some_session_id"
};

lexruntime.recognizeText(lexparams, function(err, data) {
    if (err) console.log(err, err.stack); // an error occurred
    else     console.log(data);           // successful response
});
