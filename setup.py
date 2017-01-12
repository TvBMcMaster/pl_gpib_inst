"""PL GPIB Instruments Setup File."""
from distutils.core import setup

setup(
    name="Prologix GPIB Instrument Library",
    description="A collection of Instrument classes for specific equipment to be used with the pl_gpib Prologix GPIB library. ",
    version="0.1",
    author="Tim van Boxtel",
    packages=['pl_gpib_inst']
)
