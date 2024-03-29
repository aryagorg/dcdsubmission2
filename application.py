from flask import Flask,Response,request,render_template,redirect,jsonify  
import pyodbc
from azure.storage.blob import BlockBlobService, PublicAccess

app = Flask(__name__)

STORAGE_ACCOUNT_NAME = 'dcdsub2'
STORAGE_ACCOUNT_KEY = 'N3/AfN3kAnVmf1IzyCAdI86qkKpddErZGC2NlLvhPZLJziITGjjtSrrMkMYvglU0GzZ8i4wC96Qqfehv88XuXA=='
SAS = '?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-09-02T15:45:07Z&st=2019-09-02T07:45:07Z&spr=https,http&sig=Ts4uou7v5ihElpRa%2BEtTBomRDlLqcBIpd895yVGXLeU%3D'

block_blob_service = BlockBlobService(account_name=STORAGE_ACCOUNT_NAME, account_key=STORAGE_ACCOUNT_KEY)

@app.route('/', methods=['GET', 'POST'])

def show():

    html = """<html>

                <head>
                    <title>Analyze Sample</title>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
                    <script src="https://drive.google.com/uc?export=view&id=11lZUoGHAIXvc2R85OlZJ9iynaSQ9HA_z" charset="utf-8"></script>
                </head>

                <body>
                    <script type="text/javascript">
                        function processimage() {
                            // **********************************************
                            // *** Update or verify the following values. ***
                            // **********************************************

                            // Replace <Subscription Key> with your valid subscription key.
                            var subscriptionKey = "777441aab2e544bf94f6eb80adf9f4a7";

                            // You must use the same Azure region in your REST API method as you used to
                            // get your subscription keys. For example, if you got your subscription keys
                            // from the West US region, replace "westcentralus" in the URL
                            // below with "westus".
                            //
                            // Free trial subscription keys are generated in the "westus" region.
                            // If you use a free trial subscription key, you shouldn't need to change
                            // this region.
                            var uriBase =
                                "https://southeastasia.api.cognitive.microsoft.com/vision/v2.0/analyze";

                            // Request parameters.
                            var params = {
                                "visualFeatures": "Categories,Description,Color",
                                "details": "",
                                "language": "en",
                            };

                            // Display the image.
                            //var sourceImageUrl =  document.getElementById("inputImage").value;
                            //var path = document.getElementById('fileinput').value
                            var path = document.getElementById("fileinput").files[0].name;
                            //var filename = path.replace(/^.*\\/, "");
                            var sourceImageUrl = "https://dcdsub2.blob.core.windows.net/dcd2cont/" + path;
                            document.querySelector("#sourceImage").src = sourceImageUrl;

                            // Make the REST API call.
                            $.ajax({
                                url: uriBase + "?" + $.param(params),

                                // Request headers.
                                beforeSend: function (xhrObj) {
                                    xhrObj.setRequestHeader("Content-Type", "application/json");
                                    xhrObj.setRequestHeader(
                                        "Ocp-Apim-Subscription-Key", subscriptionKey);
                                },

                                type: "POST",

                                // Request body.
                                data: '{"url": ' + '"' + sourceImageUrl + '"}',
                            })

                                .done(function (data) {
                                    // Show formatted JSON on webpage.
                                    $("#responseTextArea").val(JSON.stringify(data.description.captions[0].text, null, 2));
                                    //alert(data.description.captions[0].text);
                                })

                                .fail(function (jqXHR, textStatus, errorThrown) {
                                    // Display error message.
                                    var errorString = (errorThrown === "") ? "Error. " :
                                        errorThrown + " (" + jqXHR.status + "): ";
                                    errorString += (jqXHR.responseText === "") ? "" :
                                        jQuery.parseJSON(jqXHR.responseText).message;
                                    alert(errorString);
                                });
                        };
                    </script>
                    
                    <h1>Upload image:</h1>

                    <br><br>
                    Input file :
                    <input type="file" id="fileinput" />
                    <button id="upload-button">Upload</button>
                    <br>
                    <br>

                    <button onclick="processimage()">Analyze image</button>
                    <br><br>
                    <div id="wrapper" style="width:1020px; display:table;">
                        <div id="imageDiv" style="width:420px; display:table-cell;">
                            Source image:
                            <br><br>
                            <img id="sourceImage" width="400" />
                        </div>

                        <div id="jsonOutput" style="width:600px; display:table-cell;">
                            Description analyzed (if api doesnt return desc ,it show nothing, choose other pic):
                            <br><br>
                            <textarea id="responseTextArea" class="UIInput" style="width:580px; height:20px;"></textarea>
                        </div>
                    </div>


                    
                    <script>
                        const account = {
                            name: 'dcdsub2',
                            sas: '?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-09-05T15:55:03Z&st=2019-09-02T07:55:03Z&sip=0.0.0.0-255.255.255.255&spr=https,http&sig=iKmHhPAkez82zWOJHrwi7zStAe%2FfyuRDP%2By2zSlpVQo%3D'

                        };
                        const blobUri = 'https://' + account.name + '.blob.core.windows.net';
                        const blobService = AzureStorage.Blob.createBlobServiceWithSas(blobUri, account.sas);

                        document.getElementById('upload-button').addEventListener('click', () => {

                            console.log('upload button clicked');
                            const file = document.getElementById('fileinput').files[0];
                            blobService.createBlockBlobFromBrowserFile('dcd2cont',
                                file.name,
                                file,
                                (error, result) => {
                                    if (error) {
                                        // Handle blob error
                                        alert("fail upload!");
                                    } else {
                                        alert("upload success!");
                                    }
                                });
                        });


                    </script>
                </body>

                </html>""" 
  
    

    return Response(response = html, status = 200, mimetype = "text/html")

 
