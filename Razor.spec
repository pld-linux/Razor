#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of files for checking, reporting, and revoking spam
Summary(pl):	Zbiór plików do sprawdzania, raportowania i odrzucania spamu
Name:		Razor
Version:	2.81
Release:	1
License:	Artistic
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/razor/razor-agents-%{version}.tar.bz2
# Source0-md5:	1a21d84f3a8291f73e7f1d3dd36d9d7f
URL:		http://razor.sourceforge.net/
%if %{with autodeps}
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-Class-Fields
BuildRequires:	perl-Digest-Nilsimsa
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-URI
%endif
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Razor = %{version}-%{release}
Obsoletes:	perl-Vipuls-Razor-V1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vipul's Razor is a distributed, collaborative, spam detection, reporting,
and filtering network. The primary focus of the system is to identify
and remove all email spam from the internet. Visit the website at
<http://razor.sourceforge.net/>.

%description -l pl
Vipul's Razor jest dystrybuowaln±, tworzon± dziêki wspó³pracy sieci±,
s³u¿±c± do wykrywania spamu, raportowania i filtrowania. Podstawowym
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

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PERL5LIB=$RPM_BUILD_ROOT%{perl_vendorarch} \
	INSTALLMAN5DIR=%{_mandir}/man5

for f in admin check report revoke; do
	ln -sf razor-client $RPM_BUILD_ROOT%{_bindir}/razor-$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* BUGS README INSTALL CREDITS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*

%files -n perl-Razor
%defattr(644,root,root,755)
%{perl_vendorarch}/Razor2
%dir %{perl_vendorarch}/auto/Razor2
%dir %{perl_vendorarch}/auto/Razor2/Preproc
%dir %{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs
%attr(755,root,root) %{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs/deHTMLxs.so
%{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs/deHTMLxs.bs
%{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs/autosplit.ix
%{perl_vendorarch}/auto/Razor2/Syslog
%{_mandir}/man3/*
