#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	GeekCode
Summary:	Convert::GeekCode - convert and generate geek code sequences
Summary(pl.UTF-8):   Convert::GeekCode - generowanie i konwersja sekwencji ,,geek code''
Name:		perl-Convert-GeekCode
Version:	0.51
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8761684c417363bda5ca41fbcca8f3d5
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-YAML}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::GeekCode converts and generates Geek Code sequences (cf.
http://geekcode.com/). It supports different langugage codes and
user-customizable codesets.

%description -l pl.UTF-8
Moduł Convert::GeekCode konwertuje i generuje sekwencje Geek Code
(http://geekcode.com/). Obsługuje kody dla różnych języków i zestawy
kodów definiowane przez użytkownika.

%package -n geekcode-tools
Summary:	geekdec - Geek Code decoder, geekgen - Geek Code generator
Summary(pl.UTF-8):   geekdec - dekoder i geekgen - generator Geek Code
Group:		Applications
Requires:	%{name}

%description -n geekcode-tools
geekdec parses Geek Code sequences read from the standard input, and
prints out explanations.

geekgen generates Geek Code sequences interactively, according to
user's input. User could mix numerical selections with usual symbols
like (), >, ! and @.

%description -n geekcode-tools -l pl.UTF-8
geekdec analizuje sekwencje Geek Code czytane ze standardowego wyjścia
i wypisuje ich znaczenie.

geekgen generuje sekwencje Geek Code interaktywnie, zgodnie z danymi
wprowadzanymi przez użytkownika. Użytkownik może mieszać numery opcji
ze zwykle używanymi symbolami takimi jak (), >, ! i @.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*

%files -n geekcode-tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
