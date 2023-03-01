# Ambisonics algorithm

import numpy as np

def ambisonics_algorithm(audio_data, ambisonic_coefficients):
    """
    Applies the Ambisonics algorithm to audio data and Ambisonic coefficients to produce a 3D sound field.

    Parameters:
    audio_data (numpy array): audio samples of shape (num_samples, num_channels)
    ambisonic_coefficients (numpy array): Ambisonic coefficients of shape (num_samples, num_coefficients)

    Returns:
    numpy array: sound pressure at a point in space of shape (num_samples,)
    """
    num_samples, num_channels = audio_data.shape
    num_coefficients = ambisonic_coefficients.shape[1]

    # Compute sound field in frequency domain
    sound_field = np.zeros((num_samples,))
    for k in range(num_channels):
        sound_field += np.fft.irfft(ambisonic_coefficients[:, k], n=num_samples)

    # Compute sound pressure at a point in space
    sound_pressure = np.sum(audio_data * sound_field[:, np.newaxis], axis=0)

    return sound_pressure
