Summary:	FusionDale - applied Fusion, collection of services for applications
Summary(pl.UTF-8):	FusionDale, czyli Fusion stosowany - zbiór usług dla aplikacji
Name:		FusionDale
Version:	0.8.1
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Libs/%{name}-%{version}.tar.gz
# Source0-md5:	74c0b7e6a11e9e2f81b4d5d50095859b
URL:		http://www.directfb.org/index.php?path=Platform/FusionDale
BuildRequires:	DirectFB-devel >= 1:1.1.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FusionDale is applied Fusion and will be a collection of different
services for use by applications and other libraries (like Coma
component manager or messaging API).

%description -l pl.UTF-8
FusionDale to Fusion stosowany, biblioteka mająca być zbiorem różnych
usług przeznaczonych do wykorzystywania przez aplikacje i inne
biblioteki (takich jak zarządca komponentów Coma czy API do
komunikacji).

%package devel
Summary:	Header files for the FusionDale
Summary(pl.UTF-8):	Pliki nagłówkowe dla FusionDale
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	DirectFB-devel >= 1:1.1.0

%description devel
Header files required for development using FusionDale.

%description devel -l pl.UTF-8
Pliki nagłówkowe wymagane do tworzenia programów z użyciem
FusionDale.

%package static
Summary:	Static FusionDale library
Summary(pl.UTF-8):	Statyczna biblioteka FusionDale
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static FusionDale library.

%description static -l pl.UTF-8
Statyczna biblioteka FusionDale.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post 	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README docs/html/[!M]*
%attr(755,root,root) %{_bindir}/fddump
%attr(755,root,root) %{_bindir}/fdmaster
%attr(755,root,root) %{_libdir}/libfusiondale-0.8.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfusiondale-0.8.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfusiondale.so
%{_libdir}/libfusiondale.la
%{_includedir}/fusiondale
%{_pkgconfigdir}/fusiondale.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libfusiondale.a