%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-prbt-hardware-support
Version:        0.5.13
Release:        1%{?dist}
Summary:        ROS prbt_hardware_support package

License:        LGPLv3
URL:            https://wiki.ros.org/prbt_hardware_support
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-pilz-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
BuildRequires:  libmodbus-devel
BuildRequires:  ros-melodic-canopen-chain-node
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-code-coverage
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-message-filters
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-pilz-msgs
BuildRequires:  ros-melodic-pilz-testutils
BuildRequires:  ros-melodic-pilz-utils
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf2
BuildRequires:  ros-melodic-tf2-geometry-msgs
BuildRequires:  ros-melodic-tf2-ros
BuildRequires:  ros-melodic-urdf

%description
Control hardware functions of the PRBT manipulator like STO for Stop1
functionality.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Wed Dec 04 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.13-1
- Autogenerated by Bloom

* Thu Nov 28 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.12-1
- Autogenerated by Bloom

* Fri Nov 22 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.11-1
- Autogenerated by Bloom

* Tue Oct 08 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.10-1
- Autogenerated by Bloom

* Mon Oct 07 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.9-1
- Autogenerated by Bloom

* Tue Sep 10 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.8-1
- Autogenerated by Bloom

* Thu Aug 29 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.7-1
- Autogenerated by Bloom

* Wed Jun 12 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.6-1
- Autogenerated by Bloom

* Tue May 28 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.4-1
- Autogenerated by Bloom

* Thu Apr 25 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.3-1
- Autogenerated by Bloom

* Thu Feb 21 2019 Alexander Gutenkunst <a.gutenkunst@pilz.de> - 0.5.2-0
- Autogenerated by Bloom

* Fri Dec 14 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.1-2
- Autogenerated by Bloom

* Fri Dec 14 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.1-1
- Autogenerated by Bloom

* Fri Nov 30 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.1-0
- Autogenerated by Bloom

* Thu Nov 08 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.0-1
- Autogenerated by Bloom

* Wed Nov 07 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.5.0-0
- Autogenerated by Bloom

