#
# Conditional build:
# _without_autodeps	- don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of files for checking, reporting, and revoking spam
Summary(pl):	Zbiór plików do sprawdzania, raportowania i odrzucania spamu
Name:		Razor
Version:	2.12
Release:	4
License:	Artistic
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/sourceforge/razor/razor-agents-%{version}.tar.gz
# Source0-md5:	1528a40a7ce0929971f2b745b5e88ee9
Patch0:		razor-agents-makefile.patch
URL:		http://razor.sourceforge.net/
BuildRequires:	perl-devel >= 5.8.0
%if 0%{!?_without_autodeps:1}
BuildRequires:	perl-Class-Fields
BuildRequires:	perl-Digest-Nilsimsa
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-URI
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Razor = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	perl-Vipuls-Razor-V1

%description
Vipul's Razor is a distributed, collaborative, spam detection, reporting,
and filtering network.  The primary focus of the system is to identify
and remove all email spam from the internet.  Visit the website at
<http://razor.sourceforge.net/>.

%description -l pl
Vipul's Razor jest dystrybuowaln±, tworzon± dziêki wspó³pracy sieci±,
s³u¿±c± do wykrywania spamu, raportowania i filtrowania.  Podstawowym
zadaniem systemu jest identyfikacja spamu z poczty internetowej.
Odwied¼ stronê domow±: <http://razor.sourceforge.net/>.

%package -n perl-Razor
Summary:	Perl modules for Razor
Summary(pl):	Modu³y Perla dla Razora
Group:		Development/Languages/Perl

%description -n perl-Razor
Perl modules for Razor, class Razor2::.

%description -n perl-Razor -l pl
Modu³y Perla dla Razora, klasa Razor2::.

%prep
%setup -q -n razor-agents-%{version}
%patch -p0

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

#%%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

for f in check register report revoke; do
	ln -sf razor-client $RPM_BUILD_ROOT%{_bindir}/razor-$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* BUGS README INSTALL CREDITS
%{_bindir}/*
%{_mandir}/man[15]/*

%files -n perl-Razor
%defattr(644,root,root,755)
%{perl_vendorlib}/Razor2
%{_mandir}/man3/*
