from setuptools import find_packages, setup

package_name = 'trucon_camera'

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
    maintainer='piys',
    maintainer_email='het203007@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'camera_node = trucon_camera.camera_node:main',
            'vision_node = trucon_camera.vision_node:main',
	    'arm_control_node = trucon_camera.arm_control_node:main',
        ],
    },
)
