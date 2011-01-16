Summary:	Demo of the fprint drivers
Name:		fprint_demo
Version:	0.4
Release:	1
License:	GPL v2
Group:		Base
URL:		http://www.reactivated.net/fprint/wiki/Main_Page
Source0:	http://downloads.sourceforge.net/fprint/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Source2:	fprint-icon.png
BuildRequires:	gtk+2-devel
BuildRequires:	libfprint-devel
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphical tool to demonstrate how works for the fprint drivers

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/fprint-icon.png
