## Installation

To install the [`chirp_spectrogram_generator`](https://pypi.org/project/chirp-spectrogram-generator/) package, run the following command:

```bash
pip install chirp-spectrogram-generator
```
---

#### [100,000 Generated Chirp Spectrograms with Corresponding Labels – Ready for Your ML/DL Pipeline!](https://huggingface.co/datasets/nubahador/ChirpLoc100K___A_Synthetic_Spectrogram_Dataset_for_Chirp_Localization/blob/main/README.md)

<div style="display: flex; flex-wrap: wrap; gap: 15px; margin-top: 15px;">
    <div style="flex: 1; min-width: 200px; background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h4 style="margin-top: 0; color: #5f6368;">🧑‍💻 Curated by</h4>
        <p>Nooshin Bahador</p>
    </div>
    <div style="flex: 1; min-width: 200px; background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h4 style="margin-top: 0; color: #5f6368;">💰 Funded by</h4>
        <p>Canadian Neuroanalytics Scholars Program</p>
    </div>
</div>
</div>

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin-bottom: 20px; border-left: 4px solid #ea4335;">
<h2 style="margin-top: 0;">🔗 Dataset Sources</h2>
<div style="display: flex; flex-wrap: wrap; gap: 15px;">
    <div style="flex: 1; min-width: 250px; background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
        <h4 style="margin-top: 0;">Research Paper</h4>
        <p><a href="https://arxiv.org/pdf/2503.22713">ArXiv Publication</a></p>
    </div>
</div>
</div>

<div style="background: #f8f9fa; border-radius: 8px; padding: 20px; margin-bottom: 20px; border-left: 4px solid #673ab7;">
<h2 style="margin-top: 0;">📄 Citation</h2>
<div style="background: white; border-radius: 8px; padding: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
    <p>Bahador, N., & Lankarany, M. (2025). Chirp localization via fine-tuned transformer model: A proof-of-concept study. arXiv preprint arXiv:2503.22713. <a href="https://arxiv.org/pdf/2503.22713">[PDF]</a></p>
</div>
</div>

<div style="margin-top: 15px; padding-top: 15px; border-top: 1px solid #e0e0e0;">
    <h4 style="margin-bottom: 5px;">Dataset Card Authors</h4>
    <p><a href="https://www.linkedin.com/in/nooshin-bahador-30348950/">Nooshin Bahador</a></p>
</div>
</div>

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
