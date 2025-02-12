# snatch_name.py

## Description
`snatch_name.py` is a simple Python script that extracts the gene name corresponding to a given gene ID from a GTF file. The script reads the file line by line, searching for the provided gene ID and retrieving its associated gene name.

## Usage

Run the script from the command line with the following syntax:

```bash
python snatch_name.py <gene_id> <filename>
```

### Example

```bash
python snatch_name.py ENSMUSG00000051951 genes.gtf
```

### Output
If the gene ID is found in the GTF file, the script prints the corresponding gene name. Additionally, it reports the script execution time.

## Requirements
- Python 3.x

## Installation
Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/YOUR-USERNAME/bioinformatics-task.git
cd bioinformatics-task
```

## File Structure
```
bioinformatics-task/
│── snatch_name.py  # Main script
│── README.md       # Documentation
│── LICENSE         # License file
│── .gitignore      # Ignored files
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## .gitignore
```
__pycache__/
*.log
*.csv
*.tsv
*.gz
.DS_Store
```

## LICENSE
```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

(Full MIT license text here...)
```
