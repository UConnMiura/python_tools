# python_tools
Some tools for wrangling genomics data

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
