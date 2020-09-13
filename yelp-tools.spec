Summary:	Tools to create, manage, and publish documentation for Yelp
Summary(pl.UTF-8):	Narzędzia do tworzenia, zarządzania i publikowania dokumentacji dla Yelpa
Name:		yelp-tools
Version:	3.38.0
Release:	1
License:	GPL v2+ with exceptions
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/yelp-tools/3.38/%{name}-%{version}.tar.xz
# Source0-md5:	44ed3d4824a0a96ef45a13a1c79850a1
Patch0:		%{name}-sh.patch
URL:		https://wiki.gnome.org/Apps/Yelp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	itstool
BuildRequires:	libxml2-progs >= 1:2.6.12
BuildRequires:	libxslt-progs >= 1.1.8
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-xsl >= 3.18.0
Requires:	itstool
Requires:	libxml2-progs >= 1:2.6.12
Requires:	libxslt-progs >= 1.1.8
Requires:	yelp-xsl >= 3.38.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
yelp-tools is a collection of scripts and build utilities to help
create, manage, and publish documentation for Yelp and the web. Most
of the heavy lifting is done by packages like yelp-xsl and itstool.
This package just wraps things up in a developer-friendly way.

%description -l pl.UTF-8
yelp-tools to zestaw skryptów i narzędzi do budowania, mających
pomagać przy tworzeniu, zarządzaniu i publikowaniu dokumentacji dla
Yelpa oraz na WWW. Większość pracy wykonywana jest przez pakiety
takie jak yelp-xsl i itstool. Ten pakiet po prostu obudowuje je w
sposób przyjazny dla programisty.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/yelp-build
%attr(755,root,root) %{_bindir}/yelp-check
%attr(755,root,root) %{_bindir}/yelp-new
%{_aclocaldir}/yelp.m4
%{_datadir}/yelp-tools
