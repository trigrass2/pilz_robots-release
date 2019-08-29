Name:           ros-melodic-prbt-support
Version:        0.5.7
Release:        1%{?dist}
Summary:        ROS prbt_support package

Group:          Development/Libraries
License:        Apache 2.0
URL:            https://wiki.ros.org/prbt_support
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-canopen-motor-node
Requires:       ros-melodic-controller-manager
Requires:       ros-melodic-joint-state-controller
Requires:       ros-melodic-pilz-control
Requires:       ros-melodic-prbt-hardware-support
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rosservice
Requires:       ros-melodic-topic-tools
Requires:       ros-melodic-xacro
BuildRequires:  clang-tools-extra
BuildRequires:  eigen3-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-joint-state-publisher
BuildRequires:  ros-melodic-moveit-core
BuildRequires:  ros-melodic-moveit-ros-planning
BuildRequires:  ros-melodic-prbt-hardware-support
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslaunch
BuildRequires:  ros-melodic-rostest
BuildRequires:  ros-melodic-rviz

%description
Mechanical, kinematic and visual description of the Pilz light weight arm PRBT.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
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

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
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

* Wed Aug 15 2018 Pilz GmbH and Co. KG <ros@pilz.de> - 0.3.0-0
- Autogenerated by Bloom

