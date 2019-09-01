from flask import Flask,Response,request,render_template,redirect,jsonify  
from flask_cors import CORS
import pyodbc
#import azure.common
#from azure.storage import CloudStorageAccount

app = Flask(__name__)

STORAGE_ACCOUNT_NAME = 'dcdsub2'
STORAGE_ACCOUNT_KEY = 'N3/AfN3kAnVmf1IzyCAdI86qkKpddErZGC2NlLvhPZLJziITGjjtSrrMkMYvglU0GzZ8i4wC96Qqfehv88XuXA=='
# SAS = '?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2020-09-01T18:13:18Z&st=2019-09-01T10:13:18Z&sip=0.0.0.0-255.255.255.255&spr=https&sig=kXVjVZeTigyHW7%2FYGW63BGkMDpNQz8MQUI7P43e6Jno%3D'

account = CloudStorageAccount(STORAGE_ACCOUNT_NAME, STORAGE_ACCOUNT_KEY)

@app.route('/', methods=['GET'])
def show():

    html = """<html>
                <head>
                    <title>Submission 2</title>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
                    <script src="https://drive.google.com/uc?export=view&id=11lZUoGHAIXvc2R85OlZJ9iynaSQ9HA_z" charset="utf-8"></script>
                </head>
                <body>
                
                <script type="text/javascript">
                    function processImage() {
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
                        var sourceImageUrl = document.getElementById("inputImage").value;
                        document.querySelector("#sourceImage").src = sourceImageUrl;
                
                        // Make the REST API call.
                        $.ajax({
                            url: uriBase + "?" + $.param(params),
                
                            // Request headers.
                            beforeSend: function(xhrObj){
                                xhrObj.setRequestHeader("Content-Type","application/json");
                                xhrObj.setRequestHeader(
                                    "Ocp-Apim-Subscription-Key", subscriptionKey);
                            },
                
                            type: "POST",
                
                            // Request body.
                            data: '{"url": ' + '"' + sourceImageUrl + '"}',
                        })
                
                        .done(function(data) {
                            // Show formatted JSON on webpage.
                            $("#responseTextArea").val(JSON.stringify(data, null, 2));
                        })
                
                        .fail(function(jqXHR, textStatus, errorThrown) {
                            // Display error message.
                            var errorString = (errorThrown === "") ? "Error. " :
                                errorThrown + " (" + jqXHR.status + "): ";
                            errorString += (jqXHR.responseText === "") ? "" :
                                jQuery.parseJSON(jqXHR.responseText).message;
                            alert(errorString);
                        });
                    };
                </script>
                
                <h1>Analyze image:</h1>
                Enter the URL to an image, then click the <strong>Analyze image</strong> button.
                <br><br>
                Image to analyze:
                <input type="text" name="inputImage" id="inputImage"
                    value="https://upload.wikimedia.org/wikipedia/commons/3/3c/Shaki_waterfall.jpg" />
                <button onclick="processImage()">Analyze image</button>
                <br><br>
                <div id="wrapper" style="width:1020px; display:table;">
                    <div id="jsonOutput" style="width:600px; display:table-cell;">
                        Response:
                        <br><br>
                        <textarea id="responseTextArea" class="UIInput"
                                style="width:580px; height:400px;"></textarea>
                    </div>
                    <div id="imageDiv" style="width:420px; display:table-cell;">
                        Source image:
                        <br><br>
                        <img id="sourceImage" width="400" />
                    </div>
                </div>
                <button id="create-button">Create Container</button>

                <input type="file" id="fileinput" />
                <button id="upload-button">Upload</button>
                <script>
                    const account = {
                        name: 'dcdsub2',
                        sas:  '?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2020-09-01T03:04:28Z&st=2019-08-31T19:04:28Z&spr=https,http&sig=jqjtaWpiZzumf%2FAB%2BAw44DrsLp%2FU%2BH%2Baw6Clk0eZ%2Bbk%3D'
                        
                    };

                    const blobUri = 'https://' + account.name + '.blob.core.windows.net';
                    const blobService = AzureStorage.Blob.createBlobServiceWithSas(blobUri, account.sas);
                    
                    document.getElementById('create-button').addEventListener('click', () => {
                        
                        console.log('create button clicked');
                        blobService.createContainerIfNotExists('mycontainer',  (error, container) => {
                            if (error) {
                                // Handle create container error
                                console.log('fail creating container');
                            } else {
                                console.log(container.name);
                            }
                        });

                    });

                    document.getElementById('upload-button').addEventListener('click', () => {
                        
                        console.log('upload button clicked');
                        const file = document.getElementById('fileinput').files[0];
                        blobService.createBlockBlobFromBrowserFile('dcdcont2', 
                                                                    file.name, 
                                                                    file, 
                                                                    (error, result) => {
                                                                        if(error) {
                                                                            // Handle blob error
                                                                            console.log('fail upload blob');
                                                                        } else {
                                                                            console.log('Upload is successful');
                                                                        }
                                                                    });

                        });
                      </script>
                      <script type=text/javascript>
                            $(function() {
                              $('a#test').bind('click', function() {
                                $.getJSON('/createcont',
                                    function(data) {
                                  //do nothing
                                });
                                return false;
                              });
                            });
                    </script>
                      
                </body>
                </html>""" 

    

    return Response(response = html, status = 200, mimetype = "text/html")

# @app.route('/createcont', methods=['POST'])
# def createcont():
#     # Create a Block Blob Service object
#     blockblob_service = account.create_block_blob_service()
#     #blockblob_service = BlockBlobService(account_name=config.STORAGE_ACCOUNT_NAME, account_key=config.STORAGE_ACCOUNT_KEY)
#     container_name = 'blockblobbasicscontainer' + \
#         blob_samples.randomcontainername(6)

#     # Create a new container
#     print('1. Create a container with name - ' + container_name)
#     blockblob_service.create_container(container_name)


