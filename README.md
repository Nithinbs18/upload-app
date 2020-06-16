# Upload-app

This is a simple upload application built using HTML, Bootstrap, and Flask as backend. The upload of a file is possible only if the file size is below 1MB, there are 2 places this is verified i.e. the submit button is active only if the file size is less than 1MB also in the backend there is a check again to verify the size if verified then the POST is made to the AWS endpoint.
