Name:           dde-appearance
Version:        1.0.0
Release:        1%{?dist}
Summary:        DDE Appearance Settings for Lingmo OS
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/dde-appearance
Source0:        dde-appearance-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(dtk6core)
BuildRequires:  pkgconfig(dtk6gui)
BuildRequires:  pkgconfig(dtk6widget)

%description
DDE Appearance provides theme and appearance customization
for the Lingmo desktop environment, including icons, wallpapers,
and cursor themes.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%doc README.md
%license LICENSE*
%{_bindir}/dde-appearance
%{_libdir}/dde-appearance/
%{_datadir}/dde-appearance/
%{_datadir}/dbus-1/services/*.service

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
