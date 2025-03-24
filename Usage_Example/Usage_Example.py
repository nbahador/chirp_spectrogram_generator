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
