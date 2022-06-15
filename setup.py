#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'neon-keyword-plugin-RAKE=neon_keyword_plugin_RAKE:RAKEExtractor'
setup(
    name='neon-keyword-plugin-RAKE',
    version='0.0.1',
    description='A keyword extractor for ovos/neon/mycroft',
    url='https://github.com/NeonGeckoCom/neon-keyword-plugin-RAKE',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='bsd3',
    packages=['neon_keyword_plugin_RAKE'],
    zip_safe=True,
    keywords='mycroft plugin keyword extractor',
    entry_points={'intentbox.keywords': PLUGIN_ENTRY_POINT}
)
