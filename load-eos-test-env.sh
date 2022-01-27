#!/bin/bash

if [[ ! -z EAPI_CONF ]]; then
    export EAPI_CONF='tests/eapi.conf'
    echo "Load a test environment for EAPI with file located at: ${EAPI_CONF}"
fi