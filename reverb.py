# Conversion of the Convolution Reverb algorithm

import numpy as np

def convolution_reverb(input_signal, impulse_response):
    """
    Simulate the acoustic properties of a space using convolution reverb.

    Parameters:
    input_signal (numpy array): audio samples of shape (num_samples,)
    impulse_response (numpy array): impulse response samples of shape (num_ir_samples,)

    Returns:
    numpy array: output signal of shape (num_samples + num_ir_samples - 1,)
    """
    # Compute the length of the resulting output signal
    output_length = len(input_signal) + len(impulse_response) - 1

    # Pad the input signal and impulse response with zeros to the output length
    input_signal_padded = np.pad(input_signal, (0, output_length - len(input_signal)), mode='constant')
    impulse_response_padded = np.pad(impulse_response, (0, output_length - len(impulse_response)), mode='constant')

    # Perform convolution using the FFT method
    input_signal_fft = np.fft.fft(input_signal_padded)
    impulse_response_fft = np.fft.fft(impulse_response_padded)
    output_signal_fft = input_signal_fft * impulse_response_fft
    output_signal = np.real(np.fft.ifft(output_signal_fft))

    return output_signal
