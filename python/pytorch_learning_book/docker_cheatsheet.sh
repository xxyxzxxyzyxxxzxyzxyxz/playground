#!/bin/bash


case "$1" in
    "run")
        docker run \
             -it \
             --gpus all \
             -v /etc/passwd:/etc/passwd:ro \
             -v /etc/group:/etc/group:ro \
             -v ${PWD}:/home \
             -u $(id -u ${USER}):$(id -g ${USER}) \
             -p 8888:8888 \
             nvcr.io/nvidia/pytorch:22.01-py3
             /bin/bash
        ;;
    "jupyter")
        jupyter notebook \
	    --port=8888 \
	    --ip=0.0.0.0 \
	    --allow-root \
	    --no-browser \
        --NotebookApp.token=''
        ;;
    *)
        echo "undefined argment"
        ;;
esac