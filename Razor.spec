#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
Summary:	Collection of files for checking, reporting, and revoking spam
Summary(pl.UTF-8):	Zbiór plików do sprawdzania, raportowania i odrzucania spamu
Name:		Razor
Version:	2.85
Release:	8
License:	Artistic
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/razor/razor-agents-%{version}.tar.bz2
# Source0-md5:	014d08db40187cb1316482191566b012
URL:		http://razor.sourceforge.net/
%if %{with autodeps}
BuildRequires:	perl-Class-Fields
BuildRequires:	perl-Digest-Nilsimsa
BuildRequires:	perl-Digest-SHA1
BuildRequires:	perl-Net-DNS
BuildRequires:	perl-URI
%endif
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Razor = %{version}-%{release}
Obsoletes:	perl-Vipuls-Razor-V1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vipul's Razor is a distributed, collaborative, spam detection,
reporting, and filtering network. The primary focus of the system is
to identify and remove all email spam from the internet.

%description -l pl.UTF-8
Vipul's Razor jest dystrybuowalną, tworzoną dzięki współpracy siecią,
służącą do wykrywania spamu, raportowania i filtrowania. Podstawowym
zadaniem systemu jest identyfikacja spamu z poczty internetowej.

%package -n perl-Razor
Summary:	Perl modules for Razor
Summary(pl.UTF-8):	Moduły Perla dla Razora
Group:		Development/Languages/Perl

%description -n perl-Razor
Perl modules for Razor, class Razor2::.

%description -n perl-Razor -l pl.UTF-8
Moduły Perla dla Razora, klasa Razor2::.

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
install -d $RPM_BUILD_ROOT%{_sysconfdir}/razor

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/razor-agents/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* BUGS README INSTALL CREDITS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n perl-Razor
%defattr(644,root,root,755)
%dir %{_sysconfdir}/razor
%{perl_vendorarch}/Razor2
%dir %{perl_vendorarch}/auto/Razor2
%dir %{perl_vendorarch}/auto/Razor2/Preproc
%dir %{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs
%attr(755,root,root) %{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs/deHTMLxs.so
%{perl_vendorarch}/auto/Razor2/Preproc/deHTMLxs/autosplit.ix
%{perl_vendorarch}/auto/Razor2/Syslog
%{_mandir}/man3/*
