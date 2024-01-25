 #!/bin/bash
#length
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2 | tr -d '\r'
