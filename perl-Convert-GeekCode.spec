#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	GeekCode
Summary:	Convert::GeekCode - Convert and generate geek code sequences
Summary(pl):	Convert::GeekCode - Generuj i konwertuj sekwencje ,,geek code''
Name:		perl-Convert-GeekCode
Version:	0.5
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-YAML
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
B<Convert::GeekCode> converts and generates Geek Code sequences (cf.
http://geekcode.com/). It supports different langugage codes and
user-customizable codesets.

# %description -l pl
# TODO

%package -n geekcode-tools
Summary:	geekdec - Geek Code decoder, geekgen - Geek Code generator
Group:		Applications
Requires:	%{name}

%description -n geekcode-tools
geekdec parses Geek Code sequences read from the stanard input, and
prints out explanations.

geekgen generates Geek Code sequences interactively, according to user's
input. User could mix numerical selections with usual symbols like (),
>, ! and @.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{perl_sitelib}/%{pdir}/%{pnam}
%{_mandir}/man3/*

%files -n geekcode-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
