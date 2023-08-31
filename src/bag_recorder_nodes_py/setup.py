from setuptools import find_packages, setup

package_name = 'bag_recorder_nodes_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rohamzn',
    maintainer_email='rzninvo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'simple_bag_recorder = bag_recorder_nodes_py.simple_bag_recorder:main',
            'data_generator_node = bag_recorder_nodes_py.data_generator_node:main',
            'data_generator_executable = bag_recorder_nodes_py.data_generator_executable:main',
        ],
    },
)
