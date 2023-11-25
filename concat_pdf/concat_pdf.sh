#!/bin/bash
echo oie >> result.pdf
python3 concat_pdf.py "$@"
