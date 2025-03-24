## Installation

To install the [`chirp_spectrogram_generator`](https://pypi.org/project/chirp-spectrogram-generator/) package, run the following command:

```bash
pip install chirp-spectrogram-generator
```
---

### Sample Generated Spectrogram

<img src="https://github.com/nbahador/chirp_spectrogram_generator/blob/main/Usage_Example/spectrogram_4.png" alt="Sample Generated Spectrogram" width="300" height="200" />

---

### Sample Generated Label

| Chirp Start Time (s) | Chirp Start Freq (Hz) | Chirp End Freq (Hz) | Chirp Duration (s) | Chirp Type   |
|----------------------|-----------------------|---------------------|--------------------|--------------|
| 38.92107594          | 14.58740744           | 36.84728556         | 10.80687464        | exponential  |

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
