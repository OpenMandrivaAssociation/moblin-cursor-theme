%define sampledir $RPM_BUILD_ROOT/opt/sample-media/Images

Name:           moblin-cursor-theme
Version:        0.3
Release:        %mkrel 2
Summary:        Moblin X cursors icon theme

Group:          Graphics
License:        CC-BY
URL:            https://www.moblin.org
Source0:        http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: xcursorgen
BuildArch: noarch

%description
Moblin X cursors icon theme.

%prep
%setup -q -n %{name}-%{version}

%build
cd pngs
./make.sh

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} -p $RPM_BUILD_ROOT/usr/share/icons/moblin  
%{__cp} -r xcursors/* $RPM_BUILD_ROOT/usr/share/icons/moblin/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_datadir}/icons/moblin/


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-2mdv2011.0
+ Revision: 620376
- the mass rebuild of 2010.0 packages

* Wed Sep 30 2009 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2010.0
+ Revision: 451692
- fix group
- initial import (from Claudio Matsuoka and Caio Begotti, based on Fedora package)
- Created package structure for moblin-cursor-theme.

