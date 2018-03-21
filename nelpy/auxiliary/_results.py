"""Results container object to easily group, store, and load results."""

__all__ = ['ResultsContainer', 'load_pkl', 'save_pkl']

import gzip
import os
import pickle
# import inspect

class ResultsContainer(object):
    """Extremely simple namespace for passing around and pickling data."""

    def __init__(self, *args, description=None, **kwargs):
        kwargs['description'] = description

        if len(args) > 0:
            raise NotImplementedError("only keyword arguments accepted!")

        for key, val in kwargs.items():
            setattr(self, key, val)

    # def __init__(self, *args, description=None, **kwargs):
    #     kwargs['description'] = description

    #     # BEGIN very hacky code to get *args names; might break!
    #     # see http://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function
    #     frame = inspect.currentframe()
    #     frame = inspect.getouterframes(frame)[1]
    #     string = inspect.getframeinfo(frame[0]).code_context[0].strip()
    #     _args = string[string.find('(') + 1:-1].split(',')

    #     names = []
    #     for i in _args:
    #         if i.find('=') != -1:
    #             pass
    #             # names.append(i.split('=')[1].strip())
    #         else:
    #             names.append(i)

    #     for ii, arg in enumerate(args):
    #         setattr(self, names[ii], arg)
    #     # END very hacky code to get *args names; might break!

    #     for key, val in kwargs.items():
    #         setattr(self, key, val)

    #     self.description = None

    def __repr__(self):
        if self.isempty:
            return "<Empty ResultsContainer>"
        if self.n_objects == 1:
            n_str = " (" + str(self.n_objects) + " object)"
        else:
            n_str = " (" + str(self.n_objects) + " objects)"
        address_str = " at " + str(hex(id(self)))
        descr_str = ""
        if self.description is not None:
            descr_str = "\n**Description:** " + str(self.description)
        return "<ResultsContainer" + address_str + n_str + ">" + descr_str

    @property
    def isempty(self):
        """Empty ResultsContainer."""
        return self.n_objects == 0

    @property
    def n_objects(self):
        """(int) Number of objects in Results."""
        return len(list(self.__dict__.values())) - 1

    def save_pkl(self, fname, zip=True, overwrite=False, *, protocol=None):
        """Write pickled data to disk, possible compressing."""
        if os.path.isfile(fname):
            # file exists
            if overwrite:
                pass
            else:
                print('File "{}" already exists! Aborting...'.format(fname))
                return
        if zip:
            openzip = gzip.open
            with openzip(fname, "wb") as fid:
                pickle.dump(self, fid)
        else: 
            if (protocol is None):
                with open(fname, "wb") as fid:
                    pickle.dump(self, fid)
            else:
                with open(fname, "wb") as fid:
                    pickle.dump(self, fid, protocol=protocol)


def load_pkl(fname, zip=True):
    """Read pickled data from disk, possible decompressing."""
    if zip:
        openzip = gzip.open
        with openzip(fname, "rb") as fid:
            res = pickle.load(fid)
    else:
        with open(fname, "rb") as fid:
            res = pickle.load(fid)
    return res

def save_pkl(fname, res, zip=True, overwrite=False):
    """Write pickled data to disk, possible compressing."""
    if os.path.isfile(fname):
        # file exists
        if overwrite:
            pass
        else:
            print('File "{}" already exists! Aborting...'.format(fname))
            return
    if zip:
        open = gzip.open

    with open(fname, "wb") as fid:
        pickle.dump(res, fid)
