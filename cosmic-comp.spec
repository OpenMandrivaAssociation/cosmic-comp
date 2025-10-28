%undefine _debugsource_packages

Name:           cosmic-comp
Version:        1.0.0
%define beta beta.3
Release:        %{?beta:0.%{beta}.}1
Summary:        Compositor for the COSMIC DE
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/cosmic-comp
Source0:        https://github.com/pop-os/cosmic-comp/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
#Patch0:         https://patch-diff.githubusercontent.com/raw/pop-os/cosmic-comp/pull/1127.patch

%patchlist
https://github.com/pop-os/cosmic-comp/commit/3b70bc02654694d50ad1c46361b6aa1a0544b9d9.patch
https://github.com/pop-os/cosmic-comp/commit/0847247c33d54569bde1b86e42eb995104f807ec.patch
https://github.com/pop-os/cosmic-comp/commit/5e9ea938196d6f2e61b42895ddb5946377f255e7.patch
https://github.com/pop-os/cosmic-comp/commit/b6c5d00becf1571a0d81478973178c367a2524a7.patch
https://github.com/pop-os/cosmic-comp/commit/0a8da05847290439951561fd3ebae581a0e0ff5b.patch
https://github.com/pop-os/cosmic-comp/commit/1f7f0c70b7cac1f8d375c18c35f6574af5c5ab69.patch
https://github.com/pop-os/cosmic-comp/commit/586a16f17f45f9b6a3f6a36d3fb621bcc6d99d1a.patch
https://github.com/pop-os/cosmic-comp/commit/5a2eca29c38f24901a8f5f793d2190571d95c9ad.patch

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
