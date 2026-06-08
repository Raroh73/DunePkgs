%global appid io.github.kolunmi.Bazaar

Name:           bazaar
Version:        0.8.3
Release:        1%{?dist}
Summary:        New App Store for GNOME
License:        GPL-3.0-only
URL:            https://usebazaar.org/
Source:         https://github.com/bazaar-org/bazaar/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  babel
BuildRequires:  blueprint-compiler
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build

BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(glycin-gtk4-2)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libproxy-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(malcontent-0)
BuildRequires:  pkgconfig(md4c)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(xmlb)
BuildRequires:  pkgconfig(yaml-0.1)

%description
New App Store for GNOME with a focus on discovering and installing applications and add-ons from Flatpak remotes, particularly Flathub.

%prep
%autosetup

%conf
%meson

%build
%meson_build

%install
%meson_install
%find_lang %{name}
rm %{buildroot}%{_bindir}/bge-demo
rm %{buildroot}%{_libdir}/pkgconfig/bge.pc
rm -fr %{buildroot}%{_includedir}/bge/

%post
%systemd_user_post %{appid}.service

%preun
%systemd_user_preun %{appid}.service

%postun
%systemd_user_postun_with_restart %{appid}.service

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-dl-worker
%{_bindir}/%{name}-refresh-worker
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/dbus-1/services/%{appid}.service
%{_datadir}/glib-2.0/schemas/%{appid}.gschema.xml
%{_datadir}/gnome-shell/search-providers/%{appid}.search-provider.ini
%{_datadir}/icons/hicolor/scalable/apps/%{appid}.svg
%{_datadir}/icons/hicolor/symbolic/apps/%{appid}-symbolic.svg
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_libdir}/libbge.so
%{_libdir}/libbge.so.0
%{_libdir}/libbge.so.%{version}
%{_userunitdir}/%{appid}.service

%changelog
* Mon Jun 08 2026 Raroh73 <me@raroh73.com>
- Update to 0.8.3
* Sat May 23 2026 Raroh73 <me@raroh73.com>
- Update to 0.8.1
* Thu May 21 2026 Raroh73 <me@raroh73.com>
- Init at 0.8.0
