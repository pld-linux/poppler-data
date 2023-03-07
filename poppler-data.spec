Summary:	Encoding files for poppler
Summary(pl.UTF-8):	Pliki kodowań dla popplera
Name:		poppler-data
Version:	0.4.12
Release:	1
License:	distributable
Group:		Libraries
Source0:	https://poppler.freedesktop.org/%{name}-%{version}.tar.gz
# Source0-md5:	67ee4a40aa830b1f6e2560ce5f6471ba
URL:		https://poppler.freedesktop.org/
BuildRequires:	rpmbuild(macros) >= 1.446
Requires:	poppler >= 0.5.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package consists of encoding files for use with poppler. The
encoding files are optional and poppler will automatically read them
if they are present. When installed, the encoding files enables
poppler to correctly render CJK and Cyrillic properly. While poppler
is licensed under the GPL, these encoding files are copyright Adobe
and licensed much more strictly, and thus distributed separately.

%description -l pl.UTF-8
Ten pakiet zawiera pliki kodowań dla popplera. Są one opcjonalne i
poppler odczyta je automatycznie jeśli będą obecne. Jeśli są
zainstalowane pozwalają popplerowi poprawnie renderować dokumenty w
CJK i cyrylicy. O ile poppler jest na licencji GPL, to te pliki
kodowań są własnością Adobe i są na bardziej restrykcyjnej licencji,
przez co są rozprowadzane oddzielnie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING COPYING.adobe README
%attr(755,root,root) %{_datadir}/poppler
%{_npkgconfigdir}/poppler-data.pc
