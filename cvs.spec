Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(fr):	Un système pour maintenir à jour des fichiers
Summary(pl):	Concurrent Versioning System
Summary(tr):	Sürüm denetim sistemi
Name:		cvs
Version:	1.11.1p1
Release:	1
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Source0:	ftp://ftp.cvshome.org/pub/%{name}-1.11.1/%{name}-%{version}.tar.gz
Source1:	%{name}.inetd
Patch0:		%{name}-tmprace.patch
Patch1:		%{name}-info.patch
Patch2:		http://www.t17.ds.pwr.wroc.pl/~misiek/ipv6/cvs-1.11.1-20010427-ipv6.patch.gz
Patch3:		%{name}-zlib.patch
URL:		http://www.cyclic.com/
BuildRequires:	autoconf
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CVS means Concurrent Version System; it is a version control system
which can record the history of your files (usually, but not always,
source code). CVS only stores the differences between versions,
instead of every version of every file you've ever created. CVS also
keeps a log of who, when and why changes occurred, among other
aspects. CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.

%description -l de
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
Überwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software- Entwickler notwendig sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un système de
comparaison de versions de fichiers, qui peut garder une trace des
changements apportés à des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les différences, et
non l'intégralité d'un fichier récent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date à laquelle celle-ci a eu lieu. CVS est très
utile pour gérer la mise en commun des modifications apportées par
plusieurs personnes travaillant en parallèle sur les mêmes fichiers.
Au lieu de garder plusieurs versions des fichiers dans un seul
répertoire, CVS crée une série de répertoires, chacun contenant une
nouvelle version des fichiers. Ces répertoires et ces fichiers peuvent
ensuite être regroupés pour former la version la plus à jour du
logiciel. Installez ce package si vous avez besoin d'utiliser un
système de contrôle de version.

%description -l pl
CVS jest nak³adk± na rcs (Revision Control System, czyli w wolnym
t³umaczeniu system kontroli wersji zasobów), który rozszerza
mo¿liwo¶ci rcs'a z narzêdzia do kontroli zbioru plików w pojedynczym
katalogu o mo¿liwo¶æ kontroli zbioru hierarhicznie u³o¿onych katalogów
z plikami. Z pomoc± CVS w ³atwy sposób mo¿na zarz±dzaæ kodem ¼ród³owym
opracowywanym przez nawet bardzo du¿e zespó³y programistów
umo¿liwiaj±c ¶ledzenie i kontrolê wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe³nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
topluluðunun sürüm denetimini, denetimi yapýlmýþ dizinlerin hiyerarþik
topluluðuna geniþleten rcs(1) sürüm denetim sisteminin ön yüzüdür. Bu
dizin ve dosyalar, bir yazýlým yayýný oluþturma amacýyla biraraya
getirilebilir. CVS, bu yazýlým yayýnlarýnýn yönetilmesini ve kaynak
dosyalarý bakýmýnýn birden çok yazýlým geliþtiricisi tarafýndan
eþzamanlý olarak yapýlmasýný kontrol etmek için gereken iþlevleri
saðlar.

%package pserver
Summary:	rc-inetd config files to run CVS pserver
Summary(pl):	Pliki konfiguracyjne rc-ineta do postawienia pservera CVS
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz±dzanie wersjami
Requires:	rc-inetd
Prereq:		cvs

%description pserver
Config files for rc-inetd that are necessary to run CVS in pserver
mode.

%description pserver -l pl
Pliki konfiguracyjne rc-inetd niezbêdne do uruchomienia CVSa w trybie
pserver.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
autoheader
aclocal
automake
autoconf
%configure \
	--enable-server \
	--enable-client
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/sysconfig/rc-inetd,home/cvsroot}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs

gzip -9nf doc/*.ps BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README ChangeLog \
	contrib/{*.man,README,ChangeLog,intro.doc}

rm -f contrib/{.cvsignore,Makefile*,*.pl,*.sh,*.csh}

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre pserver
if [ "$1" = 1 ]; then
	# Add user and group
	getgid cvs >/dev/null 2>&1 || %{_sbindir}/groupadd -f -g 52 cvs
	id -u cvs >/dev/null 2>&1 || %{_sbindir}/useradd -g cvs -M -d /home/cvsroot -u 52 -s /bin/false cvs 2>/dev/null
fi

%post pserver
if [ "$1" = 1 ]; then
	# Initialise repository
	%{_bindir}/cvs -d :local:/home/cvsroot init 
	chown -R cvs.cvs /home/cvsroot/CVSROOT
fi
if [ -f /var/lock/subsys/rc-inetd ]; then
	/etc/rc.d/init.d/rc-inetd reload
fi

%postun pserver
if [ "$1" = "0" ]; then
	# Remove user and group
	%{_sbindir}/userdel cvs 2>/dev/null
	%{_sbindir}/groupdel cvs 2>/dev/null
	if [ -f /var/lock/subsys/rc-inetd ]; then
		/etc/rc.d/init.d/rc-inetd reload
	fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.ps.gz contrib
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[158]/*
%{_infodir}/cvs*

%files pserver
%defattr(644,root,root,755)
%attr(770,root,cvs) %dir /home/cvsroot
%config(noreplace) %verify(not size mtime md5) /etc/sysconfig/rc-inetd/cvs
