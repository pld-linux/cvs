Summary:	Concurrent Versioning System
Summary(de):	Concurrent-Versioning-System
Summary(fr):	Un syst�me pour maintenir � jour des fichiers
Summary(pl):	Concurrent Versioning System
Summary(tr):	S�r�m denetim sistemi
Name:		cvs
Version:	1.11.1p1
Release:	1
License:	GPL
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz�dzanie wersjami
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
CVS ist ein Frontend f�r das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
�berwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software- Entwickler notwendig sind.

%description -l fr
"CVS" signifie "Concurrent Version System". C'est un syst�me de
comparaison de versions de fichiers, qui peut garder une trace des
changements apport�s � des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les diff�rences, et
non l'int�gralit� d'un fichier r�cent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date � laquelle celle-ci a eu lieu. CVS est tr�s
utile pour g�rer la mise en commun des modifications apport�es par
plusieurs personnes travaillant en parall�le sur les m�mes fichiers.
Au lieu de garder plusieurs versions des fichiers dans un seul
r�pertoire, CVS cr�e une s�rie de r�pertoires, chacun contenant une
nouvelle version des fichiers. Ces r�pertoires et ces fichiers peuvent
ensuite �tre regroup�s pour former la version la plus � jour du
logiciel. Installez ce package si vous avez besoin d'utiliser un
syst�me de contr�le de version.

%description -l pl
CVS jest nak�adk� na rcs (Revision Control System, czyli w wolnym
t�umaczeniu system kontroli wersji zasob�w), kt�ry rozszerza
mo�liwo�ci rcs'a z narz�dzia do kontroli zbioru plik�w w pojedynczym
katalogu o mo�liwo�� kontroli zbioru hierarhicznie u�o�onych katalog�w
z plikami. Z pomoc� CVS w �atwy spos�b mo�na zarz�dza� kodem �r�d�owym
opracowywanym przez nawet bardzo du�e zesp�y programist�w
umo�liwiaj�c �ledzenie i kontrol� wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pe�nych wersji oprogramowania (release).

%description -l tr
CVS (Concurrent Versioning System), tek bir dizindeki dosya
toplulu�unun s�r�m denetimini, denetimi yap�lm�� dizinlerin hiyerar�ik
toplulu�una geni�leten rcs(1) s�r�m denetim sisteminin �n y�z�d�r. Bu
dizin ve dosyalar, bir yaz�l�m yay�n� olu�turma amac�yla biraraya
getirilebilir. CVS, bu yaz�l�m yay�nlar�n�n y�netilmesini ve kaynak
dosyalar� bak�m�n�n birden �ok yaz�l�m geli�tiricisi taraf�ndan
e�zamanl� olarak yap�lmas�n� kontrol etmek i�in gereken i�levleri
sa�lar.

%package pserver
Summary:	rc-inetd config files to run CVS pserver
Summary(pl):	Pliki konfiguracyjne rc-ineta do postawienia pservera CVS
Group:		Development/Version Control
Group(de):	Entwicklung/Versionkontrolle
Group(pl):	Programowanie/Zarz�dzanie wersjami
Requires:	rc-inetd
Prereq:		cvs

%description pserver
Config files for rc-inetd that are necessary to run CVS in pserver
mode.

%description pserver -l pl
Pliki konfiguracyjne rc-inetd niezb�dne do uruchomienia CVSa w trybie
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
