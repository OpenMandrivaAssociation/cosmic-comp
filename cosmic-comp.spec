%undefine _debugsource_packages

Name:           cosmic-comp
Version:        1.0.0
%define beta beta.4
Release:        %{?beta:0.%{beta}.}1
Summary:        Compositor for the COSMIC DE
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/cosmic-comp
Source0:        https://github.com/pop-os/cosmic-comp/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.80
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
%make_build

%install
%make_install
install -d %{buildroot}%{_sysconfdir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}
%{_sysconfdir}/%{name}
%{_datadir}/cosmic
