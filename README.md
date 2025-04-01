## Installation

To install the [`chirp_spectrogram_generator`](https://pypi.org/project/chirp-spectrogram-generator/) package, run the following command:

```bash
pip install chirp-spectrogram-generator
```
---

#### [100,000 Generated Chirp Spectrograms with Corresponding Labels – Ready for Your ML/DL Pipeline!](https://huggingface.co/datasets/nubahador/ChirpLoc100K___A_Synthetic_Spectrogram_Dataset_for_Chirp_Localization/blob/main/README.md)

<table>
<tr>
<td style="vertical-align: top; width: 25%">
  
**Curated by**  
Nooshin Bahador

</td>
<td style="vertical-align: top; width: 20%">
  
**Funded by**  
Canadian Neuroanalytics Scholars Program

</td>
<td style="vertical-align: top; width: 25%">
  
**Research Paper**  
[ArXiv Publication](https://arxiv.org/pdf/2503.22713)

</td>
<td style="vertical-align: top; width: 30%">
  
**Citation**  
Bahador, N., & Lankarany, M. (2025). Chirp localization via fine-tuned transformer model: A proof-of-concept study. arXiv preprint arXiv:2503.22713. [[PDF]](https://arxiv.org/pdf/2503.22713)

</td>
</tr>
</table>

---

### Sample Generated Spectrogram

<div style="display: flex; justify-content: space-between; gap: 20px;">
    <img src="https://github.com/nbahador/chirp_spectrogram_generator/blob/main/Usage_Example/spectrogram_4.png" alt="Sample Generated Spectrogram" width="300" height="200" />
    <img src="https://github.com/nbahador/chirp_spectrogram_generator/blob/main/Usage_Example/Samples.jpg" alt="Sample Generated Spectrograms" width="400" height="200" />
</div>

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
