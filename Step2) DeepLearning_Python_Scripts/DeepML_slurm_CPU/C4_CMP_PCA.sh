#!/bin/sh
#SBATCH --partition=CPUQ
#SBATCH --account=share-ie-idi   # Account for consumed resources
#SBATCH --time=06-00:00:00    # Upper time limit for the job (DD-HH:MM:SS)
#SBATCH --nodes=1             # Allocate 1 nodes for the job
#SBATCH -c28
#SBATCH --mem=64G
#SBATCH --job-name="C4_CMP_PCA"
#SBATCH --output=/cluster/home/miladna/PythonProject/DeepLearning/File_TrainingData/DeepMLP_CPU/C4_CMP_PCA.txt
#SBATCH --mail-user=milad.naeimaei@ntnu.no
#SBATCH --mail-type=ALL








WORKDIR=${SLURM_SUBMIT_DIR}
cd ${WORKDIR}

echo "we are running from this directory: $SLURM_SUBMIT_DIR"
echo " the name of the job is: $SLURM_JOB_NAME"
echo "Th job ID is $SLURM_JOB_ID"
echo "The job was run on these nodes: $SLURM_JOB_NODELIST"
echo "Number of nodes: $SLURM_JOB_NUM_NODES"
echo "We are using $SLURM_CPUS_ON_NODE cores"
echo "We are using $SLURM_CPUS_ON_NODE cores per node"
echo "Total of $SLURM_NTASKS cores"

module load Python/3.10.8-GCCcore-12.2.0
source /cluster/home/miladna/PythonProject/0_virtualenv/envFourCPU/bin/activate

cd /cluster/home/miladna/PythonProject/DeepLearning/DeepMLP_Python_CPU
python C4_CMP_PCA.py



