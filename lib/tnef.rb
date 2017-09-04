require "tnef/version"
require "tnef/executable"

require "tmpdir"
require "fileutils"
require 'tempfile'
require 'pry'
module Tnef

  def self.unpack(winmail_io, &block)
    in_tmp_dir do |dir|
      temp_file = Tempfile.new('winmail')
      temp_file.write(winmail_io.read)
      temp_file.close
      begin
        `#{Tnef::Executable.path} --number-backups --save-body --body-pref th -K -f #{temp_file.path}`
      ensure
        temp_file.unlink
      end
      Dir.glob("#{dir}/*").select { |node| File.file?(node) }.sort.each do |file|
        yield(file)
      end
    end
  end

  def self.in_tmp_dir(&block)
    Dir.mktmpdir do |dir|
      FileUtils.cd(dir) do
        yield(dir)
      end
    end
  end

end
