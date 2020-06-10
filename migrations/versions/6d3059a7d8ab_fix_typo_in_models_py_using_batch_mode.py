"""fix typo in models.py, using batch mode

Revision ID: 6d3059a7d8ab
Revises: ec433c400077
Create Date: 2020-06-10 13:16:08.113786

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6d3059a7d8ab'
down_revision = 'ec433c400077'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completion_status', sa.Boolean(), nullable=True))
        batch_op.create_index(batch_op.f('ix_project_completion_status'), ['completion_status'], unique=False)
        batch_op.drop_index('ix_project_completetion_status')
        batch_op.drop_column('completetion_status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('project', schema=None) as batch_op:
        batch_op.add_column(sa.Column('completetion_status', sa.BOOLEAN(), nullable=True))
        batch_op.create_index('ix_project_completetion_status', ['completetion_status'], unique=False)
        batch_op.drop_index(batch_op.f('ix_project_completion_status'))
        batch_op.drop_column('completion_status')

    # ### end Alembic commands ###