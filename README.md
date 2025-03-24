## Installation

To install the [`Attention-Maps-Extraction`](https://pypi.org/project/Attention-Maps-Extraction/) package, run the following command:

```bash
pip install Attention-Maps-Extraction
```
---

### Sample Generated Map

<img src="https://github.com/nbahador/chirp_spectrogram_generator/blob/main/Usage_Example/spectrogram_4.png" alt="Sample Generated Spectrogram" width="200" height="200" />

---

```csv
https://raw.githubusercontent.com/nbahador/chirp_spectrogram_generator/main/Usage_Example/custom_labels.csv
```

---

### Usage Example

Here is an example of how to use this package:

```python
from chirp_spectrogram_generator import SpectrogramGenerator

# Initialize the generator
generator = SpectrogramGenerator(
    sample_rate=5000,
    duration=60.0,
    max_chirp_duration=15.0,
    num_time_bins=128,
    num_freq_bins=128,
    max_frequency=100,
    max_chirp_band=30,
    output_dir="custom_output_directory",
    labels_file="custom_labels.csv"
)

# Generate 1000 spectrograms
generator.generate_dataset(100)
```
