Summary:	Tools to create, manage, and publish documentation for Yelp
Summary(pl.UTF-8):	Narzędzia do tworzenia, zarządzania i publikowania dokumentacji dla Yelpa
Name:		yelp-tools
Version:	42.1
Release:	1
License:	GPL v2+ with exceptions
Group:		Libraries
Source0:	https://download.gnome.org/sources/yelp-tools/42/%{name}-%{version}.tar.xz
# Source0-md5:	d106655b3a8f8fc5fa71fbd3c2409cb8
Patch0:		%{name}-sh.patch
URL:		https://wiki.gnome.org/Apps/Yelp
BuildRequires:	itstool
BuildRequires:	libxml2-progs >= 1:2.6.12
BuildRequires:	libxslt-progs >= 1.1.8
BuildRequires:	meson >= 0.51.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	python3-lxml
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-xsl >= 41
Requires:	itstool
Requires:	libxml2-progs >= 1:2.6.12
Requires:	libxslt-progs >= 1.1.8
Requires:	python3-lxml
Requires:	yelp-xsl >= 41
BuildArch:	noarch
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
%patch -P0 -p1

%build
%meson \
	-Dhelp=true

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/yelp-build
%attr(755,root,root) %{_bindir}/yelp-check
%attr(755,root,root) %{_bindir}/yelp-new
%{_aclocaldir}/yelp.m4
%{_datadir}/yelp-tools
