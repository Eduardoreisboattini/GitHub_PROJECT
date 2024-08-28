def save_data(data, filename):
    """
    Saves data to a binary file in .npy format.

    Parameters
    ----------
    data : array_like
        The data to be saved.
    filename : str
        The file name to save the data to.
    """
    with open(filename, 'wb') as f:
        np.save(f, data)


def load_data(filename):
    """
    Loads data from a binary file in .npy format.

    Parameters
    ----------
    filename : str
        The file name to load the data from.

    Returns
    -------
    data : array_like
        The loaded data.
    """
    with open(filename, 'rb') as f:
        data = np.load(f)
    return data
