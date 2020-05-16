# Do not package empty debug_package
%global debug_package %{nil}

Summary: Nethserver arm configuration
Name: nethserver-arm-extra-config
Version: 1.0.0
Release: 1%{?dist}
License: GPL
Source: %{name}-%{version}.tar.gz

BuildRequires: nethserver-devtools

%description
Nethserver arm configuration

%prep
%setup -q

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%post

%preun

%postun

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog

* Sat May 16 2020 Mark Verlinde <mark.verlinde@gmail.com> - 1.1
- Extended template expansion of /etc/nethserver/eorepo.conf
  part of nethserver-base fixes, arm-dev #40

* Fri May 15 2020 Mark Verlinde <mark.verlinde@gmail.com> - 0.1.1
- First (unreleased) rpm-build