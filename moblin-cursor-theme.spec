%define sampledir $RPM_BUILD_ROOT/opt/sample-media/Images

Name:           moblin-cursor-theme
Version:        0.3
Release:        %mkrel 1
Summary:        Moblin X cursors icon theme

Group:          Graphics
License:        CC-BY
URL:            http://www.moblin.org
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
