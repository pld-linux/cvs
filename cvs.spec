#
# Conditional build:
%bcond_without	krb5	# disable krb5 support
#
Summary:	Concurrent Versioning System
Summary(de.UTF-8):	Concurrent-Versioning-System
Summary(es.UTF-8):	Control de versiones en modo concurrente
Summary(fr.UTF-8):	Un système pour maintenir à jour des fichiers
Summary(pl.UTF-8):	Concurrent Versioning System
Summary(pt_BR.UTF-8):	Controle de versões em modo concorrente
Summary(ru.UTF-8):	Система управления версиями
Summary(tr.UTF-8):	Sürüm denetim sistemi
Summary(uk.UTF-8):	Система керування версіями
Summary(zh_CN.UTF-8):	并发的版本管理系统CVS
Name:		cvs
Version:	1.12.13
Release:	6
License:	GPL
Group:		Development/Version Control
Source0:	ftp://ftp.gnu.org/non-gnu/cvs/source/feature/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	956ab476ce276c2d19d583e227dbdbea
Source1:	%{name}.inetd
Patch1:		%{name}-fixed_buffer.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-no_libnsl.patch
Patch4:		%{name}-info.patch
Patch5:		%{name}-posix.patch
Patch6:		%{name}-CAN_2005_2693.patch
Patch7:		%{name}-cvspass.patch
Patch8:		%{name}-datetime.patch
Patch9:		%{name}-getcwd.patch

# patches from debian
Patch100:	%{name}-debian-64bit-crash.patch
Patch101:	%{name}-debian-check-method-crash.patch
Patch102:	%{name}-debian-sparc.patch
Patch103:	%{name}-debian-zlib-read-compressed.patch
Patch104:	%{name}-debian-cvsrc.patch
Patch105:	%{name}-debian-date-format.patch
Patch106:	%{name}-debian-dsa-ext-pwd.patch
Patch107:	%{name}-debian-ext-exp.patch
Patch108:	%{name}-debian-extra-tags.patch
Patch109:	%{name}-debian-flag-conflicted-copies.patch
Patch110:	%{name}-debian-homedir.patch
Patch111:	%{name}-debian-import-n-X.patch
Patch112:	%{name}-debian-R-warning.patch
Patch113:	%{name}-debian-keyword-alnum.patch
Patch114:	%{name}-debian-l-opt.patch
Patch115:	%{name}-debian-newlines-commit-template.patch
Patch116:	%{name}-debian-normalize-roots.patch
Patch117:	%{name}-debian-pam.patch
Patch118:	%{name}-debian-parseopts.patch
Patch119:	%{name}-debian-perms.patch
Patch120:	%{name}-debian-server-wrapper.patch
Patch121:	%{name}-debian-repouid.patch
Patch122:	%{name}-debian-rsc2log.patch

URL:		http://www.nongnu.org/cvs/
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake >= 1:1.7.9
%{?with_krb5:BuildRequires:	krb5-devel}
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Obsoletes:	cvs-nserver-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_cvs_root	/var/lib/cvs

%description
CVS means Concurrent Version System; it is a version control system
which can record the history of your files (usually, but not always,
source code). CVS only stores the differences between versions,
instead of every version of every file you've ever created. CVS also
keeps a log of who and when made some changes and why they occurred,
among other aspects.

CVS is very helpful for managing releases and controlling the
concurrent editing of source files among multiple authors. Instead of
providing version control for a collection of files in a single
directory, CVS provides version control for a hierarchical collection
of directories consisting of revision controlled files. These
directories and files can then be combined together to form a software
release.

%description -l de.UTF-8
CVS ist ein Frontend für das RCS(1)-Revisionskontrollsystem, das den
Begriff der Revisionskontrolle von einer Sammlung von Dateien in einem
einzelnen Verzeichnis auf eine ganze Hierarchie ausweitet, bestehend
aus revisionskontrollierten Dateien. Diese Verzeichnisse und Dateien
lassen sich zu einer Software-Release kombinieren. CVS bietet die
Funktionen, die zur Verwaltung von Software-Releases und zur
Überwachung der gleichzeitigen Bearbeitung von Quelldateien durch
mehrere Software-Entwickler notwendig sind.

%description -l es.UTF-8
CVS significa "Concurrent Version System" (sistema concurrente de
control de versiones). Puede guardar la historia de sus ficheros
(normalmente, pero no necesariamente, código fuente). CVS sólo guarda
las diferencias entre las versiones, en vez de guardar cada una de las
versiones de cada fichero que haya creado. CVS también mantiene un
registro de quién y cuándo realizó un cambio, el porqué del cambio,
etc.

CVS es muy útil para manejar los releases y controlar la edición
concurrente de los ficheros fuente entre varios autores. En vez de
proveer control de versiones para una colección de ficheros en un solo
directorio, CVS la provee para una colección jerárquica de directorios
que consistan de ficheros de revisiones controladas. Esos directorios
y ficheros pueden luego ser reunidos para formar un release de
software.

%description -l fr.UTF-8
"CVS" signifie "Concurrent Version System". C'est un système de
comparaison de versions de fichiers, qui peut garder une trace des
changements apportés à des fichiers (le plus souvent, les fichiers des
sources d'un programme). CVS conserve seulement les différences, et
non l'intégralité d'un fichier récent et d'un fichier plus ancien. A
chaque modification d'un fichier, CVS garde (entre autres) le nom de
la personne ayant fait la modification, la raison justifiant cette
modification, et la date à laquelle celle-ci a eu lieu.

CVS est très utile pour gérer la mise en commun des modifications
apportées par plusieurs personnes travaillant en parallèle sur les
mêmes fichiers. Au lieu de garder plusieurs versions des fichiers dans
un seul répertoire, CVS crée une série de répertoires, chacun
contenant une nouvelle version des fichiers. Ces répertoires et ces
fichiers peuvent ensuite être regroupés pour former la version la plus
à jour du logiciel. Installez ce package si vous avez besoin
d'utiliser un système de contrôle de version.

%description -l pl.UTF-8
CVS jest nakładką na rcs (Revision Control System, czyli w wolnym
tłumaczeniu system kontroli wersji zasobów), który rozszerza
możliwości rcs'a z narzędzia do kontroli zbioru plików w pojedynczym
katalogu o możliwość kontroli zbioru hierarchicznie ułożonych
katalogów z plikami. Z pomocą CVS w łatwy sposób można zarządzać kodem
źródłowym opracowywanym przez nawet bardzo duże zespoły programistów
umożliwiając śledzenie i kontrolę wszystkich zmian w trakcie pracy nad
projektami i wypuszczaniem pełnych wersji oprogramowania (release).

%description -l pt_BR.UTF-8
CVS é um front end para o rcs(1) - revision control system - que
estende a noção de controle de revisão de uma coletânea de arquivo em
um único diretório para uma coleção hierárquica de diretórios que
contém arquivos controlados por revisão. Esses diretórios e arquivos
podem ser combinados juntos para criar uma release de software. CVS
oferece as funções necessárias para administrar essas release de
software e para controlar a edição concorrente de arquivos fonte por
múltiplos programadores.

%description -l ru.UTF-8
CVS (Concurrent Version System) - это система управления версиями,
которая умеет записать историю ваших файлов (обычно, но не всегда, это
исходные тексты). CVS сохраняет только различия между версиями вместо
каждой версии каждого файла, которая была когда-либо создана. Также
CVS хранит протокол того, кто, когда и зачем что-либо изменил.

CVS очень полезна для организации релизов и управления параллельной
правкой исходных файлов несколькими авторами. Вместо предоставления
управления версиями набора файлов в одном каталоге CVS предоставляет
управление версиями иерархического набора каталогов, состоящих из
файлов, версиями которых надо управллять. Эти файлы и каталоги могут
быть собраны вместе для формирования релиза ПО.

%description -l tr.UTF-8
CVS (Concurrent Versioning System), tek bir dizindeki dosya
topluluğunun sürüm denetimini, denetimi yapılmış dizinlerin hiyerarşik
topluluğuna genişleten rcs(1) sürüm denetim sisteminin ön yüzüdür. Bu
dizin ve dosyalar, bir yazılım yayını oluşturma amacıyla biraraya
getirilebilir. CVS, bu yazılım yayınlarının yönetilmesini ve kaynak
dosyaları bakımının birden çok yazılım geliştiricisi tarafından
eşzamanlı olarak yapılmasını kontrol etmek için gereken işlevleri
sağlar.

%description -l uk.UTF-8
CVS (Concurrent Version System) - це система керування версіями, яка
вміє записати історію ваших файлів (зазвичай, але не завжди, це
вихідні тексти). CVS зберігає тільки різницю між версіями замість
кожної версії кожного файлу, яка була колись створена. Також CVS
зберігає протокол того, хто, коли і навіщо щось змінив.

CVS дуже корисна для організацію релізів та керування паралельною
правкою визідних файлів кількома авторами. Замість надання можливості
керування версіями набору файлів в одному каталозі, CVS надає
можливість керування ієрархічним набором каталогів, що складаються з
файлів, версіями котрих треба керувати. Ці файли та каталоги можуть
бути зібрані разом для формування релізу ПЗ.

%package pserver
Summary:	rc-inetd config files to run CVS pserver
Summary(es.UTF-8):	Ficheros de configuración de rc-inetd para un servidor CVS pserver
Summary(pl.UTF-8):	Pliki konfiguracyjne rc-inetd do postawienia pservera CVS
Group:		Development/Version Control
Requires(post):	fileutils
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	%{name} = %{version}-%{release}
Requires:	rc-inetd
Provides:	group(cvs)
Provides:	user(cvs)
Obsoletes:	cvs-nserver-common
Obsoletes:	cvs-nserver-nserver
Obsoletes:	cvs-nserver-pserver

%description pserver
Config files for rc-inetd that are necessary to run CVS in pserver
mode.

%description pserver -l es.UTF-8
Los ficheros de configuración rc-inetd necesarios para ejecutar CVS en
el modo de pserver.

%description pserver -l pl.UTF-8
Pliki konfiguracyjne rc-inetd niezbędne do uruchomienia CVSa w trybie
pserver.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
# undefined reference to getpwline
#%patch106 -p1
%patch107 -p2
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1

rm -rf zlib && sed -i -e 's#zlib/Makefile##g' configure.in

# broken implementation, never use
rm lib/getcwd.c

%build
rm aclocal.m4
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-external-zlib \
	--enable-encryption \
	--enable-server \
	--enable-client \
	--enable-rootcommit \
	--with%{!?with_krb5:out}-gssapi \
	--with-tmpdir=/tmp \
	--with-rsh=%{_bindir}/ssh \
	--with-editor=/bin/vi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc/sysconfig/rc-inetd,%{_cvs_root}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/cvs

rm -f contrib/{.cvsignore,Makefile*,*.pl,*.sh,*.csh}
mv -f $RPM_BUILD_ROOT%{_datadir}/cvs/contrib/rcs2log $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%pre pserver
%groupadd -f -g 52 cvs
%useradd -g cvs -d %{_cvs_root} -u 52 -s /bin/false cvs

%post pserver
if [ "$1" = "1" ]; then
	# Initialise repository
	%{_bindir}/cvs -d :local:%{_cvs_root} init
	chown -R cvs:cvs %{_cvs_root}/CVSROOT
fi
%service -q rc-inetd reload

%postun pserver
if [ "$1" = "0" ]; then
	%userremove cvs
	%groupremove cvs
	%service -q rc-inetd reload
fi

%triggerpostun -- cvs-pserver < 1.1.13-1
echo "Warning: default cvsroot moved to %{_cvs_root}."
echo "Check your configration."

%files
%defattr(644,root,root,755)
%doc BUGS FAQ MINOR-BUGS NEWS PROJECTS TODO README
%doc ChangeLog doc/*.pdf contrib
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[158]/*
%{_infodir}/cvs*

%files pserver
%defattr(644,root,root,755)
%attr(770,root,cvs) %dir %{_cvs_root}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/cvs
