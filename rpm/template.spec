Name:           ros-melodic-pilz-robots
Version:        0.5.2
Release:        0%{?dist}
Summary:        ROS pilz_robots package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/pilz_robots
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-prbt-ikfast-manipulator-plugin
Requires:       ros-melodic-prbt-moveit-config
Requires:       ros-melodic-prbt-support
BuildRequires:  ros-melodic-catkin

%description
The metapackage

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

