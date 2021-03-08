%global debug_package %{nil}

Name:           photoflare
Version:        1.6.7
Release:        1
Summary:        Quick, simple but powerful Cross Platform image editor.
License:        GPL3
Group:          Graphics
URL:            http://photoflare.io/
Source0:        https://github.com/PhotoFlare/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  qt5-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(GraphicsMagick)
BuildRequires:  qmake5
BuildRequires:  rpm-helper
BuildRequires:  qt5-qttools
BuildRequires:  qt5-qttranslations
BuildRequires:  qt5-linguist-tools

%description
Quick, simple but powerful Cross Platform image editor.

%prep
%autosetup -p1

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install INSTALL_ROOT=%{buildroot}

# We dont need this:
rm -rf %{buildroot}%{_datadir}/pixmaps/photoflare.png

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/photoflare.png
%{_mandir}/man1/%{name}.1.*
%{_datadir}/metainfo/io.%{name}.%{name}.appdata.xml
%{_datadir}/%{name}/languages/*.qm
#{_datadir}/pixmaps/%{name}.png
