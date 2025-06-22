#!/bin/bash

# Version
if [[ -n $1 ]]; then
  version=$1
else
  echo "ERROR: no version specified." > /dev/stderr
  exit 1
fi

# URL
if [[ -n $2 && $2 != "-" ]]; then
  url=$2
else
  url=ghcr.io/toolbox-io/support-llm
fi

# Arch
if [[ -z $3 ]]; then
  arch=multi
else
  arch=single
fi

# Build & push the image
if [[ $arch == "multi" ]]; then
  docker buildx build \
    --platform linux/amd64,linux/arm64 \
    -t "$url:$version" \
    -t "$url:latest" \
    . \
    --push
else
  docker build \
    -t "$url:$version" \
    -t "$url:latest" \
    .
  docker push "$url:$version"
  docker push "$url:latest"
fi